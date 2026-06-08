<template>
  <header class="page-header">
    <div>
      <p class="eyebrow">{{ eyebrow }}</p>
      <h2>{{ title }}</h2>
      <p v-if="description" class="muted">{{ description }}</p>
    </div>
  </header>
</template>

<script setup>
defineProps({
  eyebrow: { type: String, default: '' },
  title: { type: String, required: true },
  description: { type: String, default: '' }
})
</script>
