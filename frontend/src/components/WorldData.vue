<!-- This is a Vue.js component called "WorldData" that renders a grid of "WorldDataBox"
components using the "v-for" directive. It takes in an array of "worldData"
props and passes the individual data to each "WorldDataBox" component.
The "worldData" prop is required and the "WorldDataBox" component is imported 
as a child component.
 -->

<template>
  <div class="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2">
    <WorldDataBox
      v-for="(value, key) in worldData"
      :key="key"
      :statData="{
        statKey: key.replace(/text/g, '').replace(/_/g, ' '),
        statValue: value,
      }"
    />
  </div>
</template>

<script>
import WorldDataBox from "./WorldDataBox.vue";

export default {
  name: "WorldData",
  components: { WorldDataBox },
  props: {
    worldData: {
      type: Array,
      required: true,
    },
  },
};
</script>
