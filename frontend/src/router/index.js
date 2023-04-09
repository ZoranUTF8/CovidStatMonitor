/* 
The code is defining a Vue.js router using the createRouter function
from the vue-router package. The router has several routes defined for the Home,
Statistics, and ContactCorpy components. The createWebHistory function is used
to create a history object for the router. The router is then exported for use
in other parts of the application.
*/

import { createRouter, createWebHistory } from "vue-router";
import { Home, Statistics, ContactCorpy } from "../views";

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
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
  {
    path: "/:catchAll(.*)",
    name: "NotFound",
    component: Home,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
