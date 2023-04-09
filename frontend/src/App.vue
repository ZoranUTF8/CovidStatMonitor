<!-- This is a Vue.js application that defines the template for the main App
component. It includes custom components NavBar and Footer, as well as the
router-view component, which displays the content of the current route. The
script section imports the NavBar and Footer components and registers them as
components of the App component. There is no styling defined in the style
section of this code. -->

<template>
  <NavBar />
  <router-view />
  <Footer />
</template>

<script>
import NavBar from "./components/NavBar.vue";
import Footer from "./components/Footer.vue";
export default { name: "App", components: { NavBar, Footer } };
</script>

<style></style>
