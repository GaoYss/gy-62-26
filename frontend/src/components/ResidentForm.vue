<template>
  <form class="form-grid" @submit.prevent="$emit('submit')">
    <label>
      姓名
      <input v-model="model.name" required />
    </label>
    <label>
      性别
      <select v-model="model.gender" required>
        <option value="male">男</option>
        <option value="female">女</option>
      </select>
    </label>
    <label>
      年龄
      <input v-model.number="model.age" type="number" min="1" required />
    </label>
    <label>
      房间号
      <input v-model="model.room_number" required />
    </label>
    <label>
      护理等级
      <select v-model="model.care_level" required>
        <option value="self_care">自理</option>
        <option value="assisted">介助</option>
        <option value="nursing">介护</option>
      </select>
    </label>
    <label>
      紧急联系人
      <input v-model="model.emergency_contact" required />
    </label>
    <label>
      联系电话
      <input v-model="model.emergency_phone" required />
    </label>
    <label class="span-2">
      健康备注
      <textarea v-model="model.medical_notes" rows="3"></textarea>
    </label>
    <button class="primary" type="submit">保存老人信息</button>
  </form>
</template>

<script setup>
defineProps({
  model: { type: Object, required: true }
})
defineEmits(['submit'])
</script>
