<!-- This is a Vue.js component that defines the layout and content of a website footer.
It includes a company logo and links to various pages of the website, such as Home,
Statistics, and Contact Us. The component also displays the copyright information,
which includes the name of the website creator and the year.
The styling of the component is scoped to ensure that it only applies to this specific
component. -->

<template>
  <footer class="bg-white rounded-lg shadow m-4">
    <div class="w-full max-w-screen-xl mx-auto p-4 md:py-8">
      <div class="sm:flex sm:items-center sm:justify-between ">
        <a
          href="https://corpy.co.jp/index.html"
          class="flex items-center mb-4 sm:mb-0"
        >
          <span
            class="self-center text-2xl font-semibold whitespace-nowrap dark:text-dark"
            >Corpy & Co.</span
          >
        </a>
        <ul
          class="flex flex-wrap items-center mb-6 text-sm font-medium text-gray-500 sm:mb-0 dark:text-gray-400"
        >
          <li>
            <router-link to="/home" class="mr-4 hover:underline md:mr-6">
              Home</router-link
            >
          </li>
          <li>
            <router-link
              to="/statistics"
              class="mr-4 hover:underline md:mr-6"
              aria-current="page"
              >Statistics</router-link
            >
          </li>
          <li>
            <router-link to="/contact" class="mr-4 hover:underline md:mr-6">
              Contact Us</router-link
            >
          </li>
        </ul>
      </div>
      <hr
        class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8"
      />
      <span
        class="block text-sm text-gray-500 sm:text-center dark:text-gray-400"
        >© 2023
        <a href="https://zoran-janjic.netlify.app/" class="hover:underline"
          >Zoran Janjic</a
        >. All Rights Reserved.</span
      >
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer",
};
</script>

<style scoped></style>
