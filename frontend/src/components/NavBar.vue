<!-- The code defines a Vue.js component called "NavBar" that creates a responsive
navigation bar for a website. The navigation bar includes links to different pages
of the website and a mobile menu button that appears on smaller screens.
The component uses Vue's router to handle page routing and toggles the visibility
of the mobile menu button using a data property called "showMenu".
The component also includes some basic styling using Tailwind CSS classes. -->

<template>
  <div>
    <div class="bg-lightblue-100">
      <nav
        class="container px-6 py-4 mx-auto md:flex md:justify-between md:items-center"
      >
        <div class="flex items-center justify-between">
          <router-link
            to="/home"
            class="text-xl font-bold text-gray-800 md:text-2xl hover:text-blue-400"
            >Corpy-Covid-Stat-Monitor
          </router-link>

          <!-- Mobile menu button -->
          <div @click="showMenu = !showMenu" class="flex md:hidden">
            <button
              type="button"
              class="text-gray-800 hover:text-gray-400 focus:outline-none focus:text-gray-400"
            >
              <svg viewBox="0 0 24 24" class="w-6 h-6 fill-current">
                <path
                  fill-rule="evenodd"
                  d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z"
                ></path>
              </svg>
            </button>
          </div>
        </div>

        <!-- Mobile Menu open: "block", Menu closed: "hidden" -->
        <ul
          :class="showMenu ? 'flex' : 'hidden'"
          class="flex-col mt-8 space-y-4 md:flex md:space-y-0 md:flex-row md:items-center md:space-x-10 md:mt-0"
        >
          <router-link
            to="/home"
            class="text-sm font-bold text-gray-800 hover:text-blue-400"
          >
            Home</router-link
          >
          <router-link
            to="/statistics"
            class="text-sm font-bold text-gray-800 hover:text-blue-400"
            aria-current="page"
            >Statistics</router-link
          >

          <router-link
            to="/contact"
            class="text-sm font-bold text-gray-800 hover:text-blue-400"
          >
            Contact Us</router-link
          >
        </ul>
      </nav>
    </div>
  </div>
</template>
<script>
export default {
  name: "NavBar",
  data() {
    return {
      showMenu: false,
    };
  },
};
</script>

<style scoped></style>
