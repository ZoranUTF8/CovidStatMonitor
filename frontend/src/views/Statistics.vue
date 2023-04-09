<!-- This code defines a Vue component called "Home" that displays a title and
a country selection component. The "CountrySelect" component allows the user
to select a specific country to view COVID-19 statistics for. The component
imports the "CovidApiService" for making API calls and "LoadingSpinner"
and "CountrySelect" components for displaying loading spinners and the
country selection dropdown. -->

<template>
  <div class="bg-gray-100 min-h-screen pt-5">
    <h1 class="text-4xl font-bold text-center">Specific Country Statistics</h1>
    <CountrySelect />
  </div>
</template>

<script>
import { CovidApiService } from "@/services/CovidApiService";
import LoadingSpinner from "@/components/LoadingSpinner.vue";
import CountrySelect from "@/components/CountrySelect.vue";
export default {
  name: "Home",
  components: { LoadingSpinner, CountrySelect },
};
</script>
