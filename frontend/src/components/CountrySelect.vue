<template>
  <div>
    <label
      for="country-select"
      class="block text-center mb-3 mt-5 text-3xl bold"
      >Select Country:</label
    >
    <select
      id="country-select"
      v-model="selectedCountry"
      @change="onChange"
      class="form-select mt-10 block mx-auto w-1/2 border p-3 rounded text-center"
    >
      <option disabled value="">Select Country</option>
      <option
        v-for="(country, index) in countries"
        :key="index"
        :value="country.name"
      >
        {{ country.name }}
      </option>
    </select>
    <div class="mt-10">
      <!-- SPINNER -->
      <div
        v-if="loading"
        class="flex items-center justify-center h-full absolute top-0 left-0 right-0 bottom-0 z-50"
      >
        <div class="flex items-center justify-center h-32 w-32 mt-40">
          <LoadingSpinner class="w-25 h-25 mt-50" />
        </div>
      </div>
      <div
        v-if="!loading && countryData != null"
        class="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl"
      >
        <div class="flex flex-col items-center">
          <div class="p-8 flex flex-col items-center">
            <div
              class="text-center uppercase tracking-wide text-indigo-500 font-semibold text-3xl"
            >
              Country Name:
              {{
                countryData.Country_text
                  ? countryData.Country_text
                  : "No current data"
              }}
            </div>
            <p class="mt-2 text-gray-500 text-2xl">
              Last Updated: {{ timestamp ? timestamp : "No current data" }}
            </p>
            <p class="mt-2 text-gray-500 text-2xl">
              Total Cases:
              {{
                countryData["Total Cases_text"]
                  ? countryData["Total Cases_text"]
                  : "No current data"
              }}
            </p>
            <p class="mt-2 text-gray-500 text-2xl">
              Total Recovered Cases:
              {{
                countryData["Total Recovered_text"]
                  ? countryData["Total Recovered_text"]
                  : "No current data"
              }}
            </p>
            <p class="mt-2 text-gray-500 text-2xl">
              Total Deaths:
              {{
                countryData["Total Deaths_text"]
                  ? countryData["Total Deaths_text"]
                  : "No current data"
              }}
            </p>
            <p class="mt-2 text-gray-500 text-2xl">
              New Cases:
              {{
                countryData["New Cases_text"]
                  ? countryData["New Cases_text"]
                  : "No current data"
              }}
            </p>
            <p class="mt-2 text-gray-500 text-2xl">
              Active Cases:
              {{
                countryData["Active Cases_text"]
                  ? countryData["Active Cases_text"]
                  : "No current data"
              }}
            </p>
            <p class="mt-2 text-gray-500 text-2xl">
              New Deaths:
              {{
                countryData["New Deaths_text"]
                  ? countryData["New Deaths_text"]
                  : "No current data"
              }}
            </p>
          </div>
        </div>
      </div>

      <div v-if="errorMessage" class="text-red-500 text-center mt-3 text-2xl">
        {{ errorMessage }}
      </div>
    </div>
  </div>
</template>

<script>
import { countries } from "countries-list";
import { CovidApiService } from "@/services/CovidApiService";
import LoadingSpinner from "@/components/LoadingSpinner.vue";
import moment from "moment";

export default {
  name: "CountrySelect",
  components: { LoadingSpinner },
  data() {
    return {
      countries: Object.values(countries),
      selectedCountry: "",
      loading: false,
      countryData: null,
      errorMessage: null,
    };
  },
  methods: {
    async onChange() {
      try {
        this.loading = true;
        const response = await CovidApiService.getSingleCountryStats(
          this.selectedCountry
        );
        this.countryData = response.data.data;
        this.loading = false;
        console.log(this.countryData);
      } catch (error) {
        console.log(error);
        this.errorMessage = error.message;
        this.loading = false;
      }
    },
  },
  computed: {
    timestamp: function () {
      return moment(this.countryData["Last Update"]).format(
        "MMMM Do YYYY,h:mm:ss a"
      );
    },
  },
};
</script>
