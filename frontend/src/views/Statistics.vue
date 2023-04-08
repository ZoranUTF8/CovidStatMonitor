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
