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
import moment from "moment";
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
  computed: {
    timestamp: function () {
      return moment(this.worldData["Last Update"]).format(
        "MMMM Do YYYY,h:mm:ss a"
      );
    },
  },
};
</script>
