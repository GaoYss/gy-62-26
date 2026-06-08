<template>
  <form class="form-grid" @submit.prevent="$emit('submit')">
    <label>
      标题
      <input v-model="model.title" required />
    </label>
    <label>
      级别
      <select v-model="model.level">
        <option value="info">普通</option>
        <option value="warning">重要</option>
        <option value="critical">紧急</option>
      </select>
    </label>
    <label>
      对象
      <select v-model="model.target_group">
        <option value="all">全部</option>
        <option value="families">家属</option>
        <option value="staff">员工</option>
      </select>
    </label>
    <label class="checkbox-row">
      <input v-model="model.is_active" type="checkbox" />
      当前有效
    </label>
    <label class="span-2">
      内容
      <textarea v-model="model.content" rows="4" required></textarea>
    </label>
    <button class="primary" type="submit">发布通知</button>
  </form>
</template>

<script setup>
defineProps({
  model: { type: Object, required: true }
})
defineEmits(['submit'])
</script>
