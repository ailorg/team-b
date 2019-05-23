<!-- TimeLine.vue -->
<template>
  <div>
    <ul>
      <Car v-for="tl in timelines" :timeline="tl" :key="tl.id"></Car>
    </ul>
  </div>
</template>

<script>
import Car from './Car'

export default {
  components: {
    Car
  },
  props: {
    timelines: Array,
  }
}
</script>
