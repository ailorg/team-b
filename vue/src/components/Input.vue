<template>
  <label>
    <span v-if="$slots.label"><slot name="label"></slot></span>
    <span v-else-if="label">{{ label }}</span>

    <input :type="type"
           :name="name"
           :placeholder="placeholder"
           :value="value"
           @input="updateValue"
           @focus="$emit('focus', $event)"
           @blur="$emit('blur', $event)"
    >
  </label>
</template>
<script>
  export default {
    props: {
      value: {},
      label: { type: String },
      name: { type: String, require: true },
      type: { type: String, default: 'text' },
      placeholder: { type: String, default: 'Search' }
    },

    methods: {
      updateValue (e) {
        this.$emit('input', e.target.value)
        this.$emit('change', e.target.value)
      }
    }
  }
</script>