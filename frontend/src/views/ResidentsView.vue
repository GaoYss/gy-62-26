<template>
  <section>
    <PageHeader eyebrow="档案" title="老人信息管理" description="维护老人基础信息、房间、护理等级和紧急联系人。" />

    <article class="panel">
      <h3>新增老人</h3>
      <ResidentForm :model="form" @submit="saveResident" />
      <p v-if="message" class="message">{{ message }}</p>
    </article>

    <article class="panel">
      <h3>老人列表</h3>
      <EmptyState v-if="residents.length === 0" />
      <div v-else class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>姓名</th>
              <th>房间</th>
              <th>年龄</th>
              <th>护理等级</th>
              <th>紧急联系人</th>
              <th>健康备注</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in residents" :key="item.id">
              <td>{{ item.name }}</td>
              <td>{{ item.room_number }}</td>
              <td>{{ item.age }}</td>
              <td>{{ careText[item.care_level] }}</td>
              <td>{{ item.emergency_contact }} · {{ item.emergency_phone }}</td>
              <td>{{ item.medical_notes || '无' }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </article>
  </section>
</template>

<script setup>
import { onMounted, reactive, ref } from 'vue'
import EmptyState from '../components/EmptyState.vue'
import PageHeader from '../components/PageHeader.vue'
import ResidentForm from '../components/ResidentForm.vue'
import { residentsApi } from '../services/residents'

const residents = ref([])
const message = ref('')
const careText = { self_care: '自理', assisted: '介助', nursing: '介护' }
const initialForm = {
  name: '',
  gender: 'male',
  age: 70,
  room_number: '',
  care_level: 'assisted',
  emergency_contact: '',
  emergency_phone: '',
  medical_notes: ''
}
const form = reactive({ ...initialForm })

onMounted(loadResidents)

async function loadResidents() {
  residents.value = (await residentsApi.list()).results
}

async function saveResident() {
  await residentsApi.create(form)
  Object.assign(form, initialForm)
  message.value = '老人信息已保存'
  await loadResidents()
}
</script>
