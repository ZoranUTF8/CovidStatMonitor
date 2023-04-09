<!-- The code defines a Vue component called WorldDataBox that displays a single statistic
in a box format with a title and value. The value displayed is either the statValue prop
passed to the component, or a formatted timestamp if the statKey prop equals "Last Update".
The timestamp is formatted using the moment.js library.
The component also includes hover effects and a shadow. -->


<template>
  <div
    class="bg-white overflow-hidden shadow rounded-lg cursor-pointer hover:shadow-xl"
  >
    <div class="px-4 py-5 sm:p-6">
      <dl>
        <dt class="text-sm font-medium text-gray-500 truncate">
          {{ statData.statKey }}
        </dt>
        <dd class="mt-1 text-3xl font-semibold text-gray-900">
          {{
            statData.statKey === "Last Update" ? timestamp : statData.statValue
          }}
        </dd>
      </dl>
    </div>
  </div>
</template>

<script>
import moment from "moment";
export default {
  name: "WorldDataBox",
  props: {
    statData: {
      type: Object,
      required: true,
    },
  },
  computed: {
    timestamp: function () {
      return moment(this.statData["Last Update"]).format(
        "MMMM Do YYYY,h:mm:ss a"
      );
    },
  },
};
</script>
