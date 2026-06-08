<template>
  <form class="form-grid" @submit.prevent="$emit('submit')">
    <label>
      探视老人
      <select v-model.number="model.resident_id" required>
        <option disabled value="">请选择</option>
        <option v-for="resident in residents" :key="resident.id" :value="resident.id">
          {{ resident.name }} · {{ resident.room_number }}
        </option>
      </select>
    </label>
    <label>
      家属姓名
      <input v-model="model.family_name" required />
    </label>
    <label>
      家属电话
      <input v-model="model.family_phone" required />
    </label>
    <label>
      关系
      <input v-model="model.relationship" required />
    </label>
    <label>
      探视时间
      <input v-model="model.visit_time" type="datetime-local" required />
    </label>
    <label>
      人数
      <input v-model.number="model.visitor_count" type="number" min="1" required />
    </label>
    <label>
      状态
      <select v-model="model.status">
        <option value="pending">待审核</option>
        <option value="approved">已通过</option>
        <option value="rejected">已拒绝</option>
        <option value="completed">已完成</option>
        <option value="cancelled">已取消</option>
      </select>
    </label>
    <label class="span-2">
      备注
      <textarea v-model="model.notes" rows="3"></textarea>
    </label>
    <button class="primary" type="submit">提交预约</button>
  </form>
</template>

<script setup>
defineProps({
  model: { type: Object, required: true },
  residents: { type: Array, default: () => [] }
})
defineEmits(['submit'])
</script>
