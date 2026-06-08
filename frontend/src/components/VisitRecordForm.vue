<template>
  <form class="form-grid" @submit.prevent="$emit('submit')">
    <label>
      预约
      <select v-model.number="model.appointment_id" required>
        <option disabled value="">请选择</option>
        <option v-for="item in appointments" :key="item.id" :value="item.id">
          {{ item.resident.name }} · {{ item.family_name }} · {{ formatTime(item.visit_time) }}
        </option>
      </select>
    </label>
    <label>
      签到时间
      <input v-model="model.check_in_time" type="datetime-local" required />
    </label>
    <label>
      签退时间
      <input v-model="model.check_out_time" type="datetime-local" />
    </label>
    <label>
      体温
      <input v-model="model.visitor_temperature" type="number" step="0.1" />
    </label>
    <label>
      接待员工
      <input v-model="model.staff_name" required />
    </label>
    <label class="span-2">
      探视记录
      <textarea v-model="model.summary" rows="3"></textarea>
    </label>
    <button class="primary" type="submit">登记探视记录</button>
  </form>
</template>

<script setup>
defineProps({
  model: { type: Object, required: true },
  appointments: { type: Array, default: () => [] }
})
defineEmits(['submit'])

function formatTime(value) {
  return value ? new Date(value).toLocaleString('zh-CN') : ''
}
</script>
