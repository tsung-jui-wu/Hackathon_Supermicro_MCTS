import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import("../views/About.vue"),
  },
  {
    path: "/formsend",
    name: "Formsend",
    component: () => import("../views/FormSend.vue"),
  },
  {
    path: "/render",
    name: "Render",
    component: () => import("../views/Render.vue"),
  },
  {
    path: "/rendernew",
    name: "Render (New)",
    component: () => import("../views/RenderNew.vue"),
  },
  {
    path: "/loading",
    name: "LoadingPage",
    component: () => import("../views/LoadingPage.vue"),
  },
  {
    path: "/PackingFailPage",
    name: "PackingFail",
    component: () => import("../views/PackingFail.vue"),
  },
  {
    path: "/containers",
    name: "Containers",
    component: () => import("../views/Containers.vue"),
  },
  {
    path: "/pallets",
    name: "Pallets",
    component: () => import("../views/Pallets.vue"),
  },
  {
    path: "/boxes",
    name: "Boxes",
    component: () => import("../views/Boxes.vue"),
  },
  {
    path: "/backups",
    name: "Backups",
    component: () => import("../views/Backups.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
