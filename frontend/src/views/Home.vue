<!-- This code defines a Vue component named "Home" which displays the welcome message
and statistics of COVID-19 cases in the world. It imports two components, LoadingSpinner
and WorldData, which are used to display a loading spinner and the world statistics data,
respectively. The component has a "data" object that stores information about the loading
state, world data, and error message. When the component is created,
it calls the "refreshWorldData" method to retrieve the latest world statistics data using the CovidApiService.
If successful, the world data is stored in the "worldData" array, and if there's an error,
the error message is displayed.
-->

<template>
  <div class="bg-gray-100 min-h-screen">
    <div class="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
      <!-- WELCOME TEXT -->
      <div class="lg:text-center">
        <p
          class="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl"
        >
          Welcome to our CORPY COVID-19 Statistics App
        </p>
        <p class="mt-4 max-w-2xl text-xl text-gray-500 lg:mx-auto">
          This app allows you to view up-to-date statistics on COVID-19 cases in
          the world and a specific country. Simply go to the statistics page and
          choose the country from the dropdown menu and view the latest data.
        </p>
      </div>

      <div class="mt-10">
        <!-- SPINNER -->
        <div
          v-if="loading"
          class="flex items-center justify-center h-full w-full fixed top-0 left-0 right-0 bottom-0 z-50 bg-gray-900 bg-opacity-50"
        >
          <div class="flex items-center justify-center h-32 w-32">
            <LoadingSpinner class="w-25 h-25" />
          </div>
        </div>

        <!-- ERROR MESSAGE -->
        <div v-if="!loading && errorMessage" class="text-center mt-10">
          <div class="container">
            <div class="row">
              <div class="h3 text-red-500 fw-bold text-4xl">
                <p>{{ errorMessage }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- WORLD DATA DISPLAY -->
        <div v-if="!loading && !errorMessage" class="mt-10">
          <h3 class="text-lg font-medium text-gray-900">World Statistics</h3>
          <WorldData :worldData="worldData" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { CovidApiService } from "@/services/CovidApiService";
import LoadingSpinner from "@/components/LoadingSpinner.vue";
import WorldData from "@/components/WorldData.vue";
export default {
  name: "Home",
  components: { LoadingSpinner, WorldData },
  data: function () {
    return { loading: false, worldData: [], errorMessage: null };
  },
  created: async function () {
    await this.refreshWorldData();
  },
  methods: {
    async refreshWorldData() {
      try {
        this.loading = true;
        const worldDataResponse = await CovidApiService.getWorldData();
        this.worldData = worldDataResponse.data.data;
        this.loading = false;
      } catch (error) {
        this.errorMessage = error.message;
        this.loading = false;
      }
    },
  },
};
</script>
