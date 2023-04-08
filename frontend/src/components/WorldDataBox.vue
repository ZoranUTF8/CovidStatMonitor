<template>
  <div class="bg-white overflow-hidden shadow rounded-lg">
    <div class="px-4 py-5 sm:p-6">
      <dl>
        <dt class="text-sm font-medium text-gray-500 truncate">
          {{ statData.statKey }}
        </dt>
        <dd class="mt-1 text-3xl font-semibold text-gray-900">
          {{ statData.statValue }}
        </dd>
      </dl>
    </div>
  </div>
</template>

<script>
export default {
  name: "WorldDataBox",
  props: {
    statData: {
      type: Object,
      required: true,
    },
  },
};
</script>
