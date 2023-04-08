import { createRouter, createWebHistory } from "vue-router";
import { Home, Statistics, ContactCorpy } from "../views";

const routes = [
  {
    path: "/home",
    name: "home",
    component: Home,
  },
  {
    path: "/statistics",
    name: "statistics",
    component: Statistics,
  },
  {
    path: "/contact",
    name: "contact",
    component: ContactCorpy,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
