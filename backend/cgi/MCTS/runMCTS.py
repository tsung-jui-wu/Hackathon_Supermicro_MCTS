import copy
import json
from os import stat

from numpy.lib.type_check import typename
from .containerMCTS import ContainerMCTS
from .Container import Container
from .helper import simulateBoxData, writeContainerDataToFile, renderContainerData

def MonteCarloTreeSearch(inputs, SimulateBoxes=False):
    #input from json

    boxes = [
        {
            "length" : b["size"][0], 
            "height" : b["size"][1],
            "width" : b["size"][2],
            "ID" : b["ID"],
            "TypeName" : b["TypeName"],
            "Weight" : b["Weight"]
        } for b in inputs["box"]]

    boxes_cbm = sum([b["length"] * b["height"] * b["width"] for b in boxes])

    CONTAINER_DIMENSIONS = {"length": inputs["container"]["size"][0], "width": inputs["container"]["size"][1], "height": inputs["container"]["size"][2]} 
    container_cbm = CONTAINER_DIMENSIONS["length"] * CONTAINER_DIMENSIONS["width"] * CONTAINER_DIMENSIONS["height"]
    container_cbm /= 1000000

    SPACE_SCALING_FACTOR = 1
    NUMBER_OF_BOXES = len(boxes)

    # input from json
    if SimulateBoxes:
        NUMBER_OF_BOXES = 300
        MIN_EDGE_SIZE = 20
        MAX_EDGE_SIZE = 60
        
        # simulateBoxData(number, min_size, max_size, box_scaling factor, save data)
        boxes, boxes_cbm = simulateBoxData(NUMBER_OF_BOXES, MIN_EDGE_SIZE, MAX_EDGE_SIZE, 1, False)
    
    

    # boxes: list of dictionaries with ['X', 'Y', 'Z']
    # boxes_cbm: total volume of boxes
    
    

    #boxes, boxes_cbm = helper.loadBoxData("Exp-20190811-182311")
    #boxes, boxes_cbm = helper.loadBoxData("Exp-20190808-121904")

    container = Container(
        id=inputs["container"]["ID"],
        typename=inputs["container"]["TypeName"]+"_0",
        weight_limmit=inputs["container"]["weight_limit"],
        length=CONTAINER_DIMENSIONS["length"],
        width=CONTAINER_DIMENSIONS["width"],
        height=CONTAINER_DIMENSIONS["height"],
        boxes=boxes,
        spaceOptimizationFactor=SPACE_SCALING_FACTOR,
        useDeepSearch=False)

    noMCTS_seq_container = copy.deepcopy(container)
    noMCTS_rnd_container = copy.deepcopy(container)

    containerMCTS = ContainerMCTS(container=container, maxIterations=50, explorationConstant=0.25)

    bestNode = containerMCTS.fill()
    bestContainer = bestNode.projectedContainer
    nodeCBM = bestNode.totalCBM

    while bestNode is not None:
        bestContainer = bestNode.projectedContainer
        bestNode = containerMCTS.getBestLeaf(bestNode, explorationConstant=0)

    if bestContainer is not None:
        data = bestContainer.getResultsJSON()
        writeContainerDataToFile(data)

    print("Boxes at hand %s @ %sCBM" % (NUMBER_OF_BOXES, boxes_cbm))

    print("Container Dimensions: L:%s H:%s W:%s @ %sCBM" % (data["dimensions"]["length"], data["dimensions"]["height"], data["dimensions"]["width"], data["containerCBM"]))
    print("Scaled container dimensions: %s" % (data["scaledDimensions"]))
    print("----------------------------------")
    print("Node CBM is %s" % nodeCBM)
    print("Projected CBM: %sCBM w/ %s boxes" % (data["cbm"], len(data["boxes"])))
    print("----------------------------------")

    noMCTS_seq_container.placeBoxesSequentially()
    seq_cnt = noMCTS_seq_container.getResultsJSON()
    print("NON-MCTS Seq Total calc'ed: %sCBM" % (seq_cnt["cbm"]))

    noMCTS_rnd_container.placeBoxesRandomly()
    rnd_cnt = noMCTS_seq_container.getResultsJSON()
    print("NON-MCTS Rand Total calc'ed: %sCBM" % (rnd_cnt["cbm"]))

    print("********************************")
    print(rnd_cnt)

    rjson = {
        "status": 130,
        "total_container_types": inputs["total_container_types"],
        "total_pallet_types": inputs["total_pallet_types"],
        "total_box_types": inputs["total_box_types"] 
    }

    container = {
        "ID": rnd_cnt["dimensions"]["ID"],
        "TypeName" : rnd_cnt["dimensions"]["TypeName"],
        "TypeIndex": rnd_cnt["dimensions"]["TypeIndex"],
        "X": rnd_cnt['dimensions']['length'],
        "Y": rnd_cnt['dimensions']['height'],
        "Z": rnd_cnt['dimensions']['width'],
        "Weight_limmit": rnd_cnt["dimensions"]["Weight_limmit"]
    }

    typeindex = set()
    filled_items_box = []
    for idx, j in enumerate(rnd_cnt['boxes']):
        dic = {
            'ID': j["box"]['ID'],
            "TypeName": j["box"]["TypeName"]+"_{}".format(idx),
            "X": j["box"]["length"],
            "Y": j["box"]["height"],
            "Z": j["box"]["width"],
            "Weight": j["box"]["Weight"],
            "position_x": j["location"]["x"],
            "position_y": j["location"]["y"],
            "position_z": j["location"]["z"],
            "RotateType": 0,
            "TypeIndex": list(typeindex).index(j["box"]["TypeName"]) if j["box"]["TypeName"] in typeindex else len(typeindex)
        }
        filled_items_box.append(dic)

    pallet_dic = {
        "ID": "testing",
        "TypeName": "122X102_0",
        "X": 122,
        "Y": 12,
        "Z": 102,
        "Weight": 1.0,
        "position_x": 0,
        "position_y": 0,
        "position_z": 0,
        "RotationType": 0,
        "TypeIndex": 0
    }

    pallet_dic["Fitted_items"] = filled_items_box
    container["Fitted_items"] = pallet_dic
    rjson["containers"] = container

    print('---------------rjson------------------')
    print(rjson)

    print("================rjson2=====================")
    rjson2 = json.dumps(rjson)
    print(rjson2)

    print("rendering data")
    renderContainerData(data)
    
    return rjson2

    #helper.renderContainerData(seq_cnt)

if __name__ == "__main__":
    MonteCarloTreeSearch()