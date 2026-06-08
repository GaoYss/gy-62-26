<template>
  <div class="empty-state">
    <strong>{{ title }}</strong>
    <span>{{ description }}</span>
  </div>
</template>

<script setup>
defineProps({
  title: { type: String, default: '暂无数据' },
  description: { type: String, default: '提交表单后会显示在这里。' }
})
</script>
