<template>
  <p>{{timeline.date}} - {{timeline.event}}</p>
</template>

<script>
export default {
  props: {
    timeline: Object,
  }
}
</script>