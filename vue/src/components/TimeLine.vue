<!-- TimeLine.vue -->
<template>
  <div>
    <ul>
      <Car v-for="le in lectures" :lecture="le" :key="le.id"></Car>
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
    lectures: Array,
  }
}
</script>
