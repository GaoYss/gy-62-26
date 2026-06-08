<template>
  <section>
    <PageHeader eyebrow="记录" title="探视记录" description="登记签到、签退、体温、接待员工和探视摘要。" />

    <article class="panel">
      <h3>新增探视记录</h3>
      <VisitRecordForm :model="form" :appointments="appointments" @submit="saveVisit" />
      <p v-if="message" class="message">{{ message }}</p>
    </article>

    <article class="panel">
      <h3>记录列表</h3>
      <EmptyState v-if="visits.length === 0" />
      <div v-else class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>老人</th>
              <th>家属</th>
              <th>签到</th>
              <th>签退</th>
              <th>体温</th>
              <th>接待员工</th>
              <th>摘要</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in visits" :key="item.id">
              <td>{{ item.appointment.resident.name }}</td>
              <td>{{ item.appointment.family_name }}</td>
              <td>{{ formatTime(item.check_in_time) }}</td>
              <td>{{ item.check_out_time ? formatTime(item.check_out_time) : '未签退' }}</td>
              <td>{{ item.visitor_temperature || '未登记' }}</td>
              <td>{{ item.staff_name }}</td>
              <td>{{ item.summary || '无' }}</td>
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
import VisitRecordForm from '../components/VisitRecordForm.vue'
import { appointmentsApi } from '../services/appointments'
import { visitsApi } from '../services/visits'

const visits = ref([])
const appointments = ref([])
const message = ref('')
const initialForm = {
  appointment_id: '',
  check_in_time: '',
  check_out_time: '',
  visitor_temperature: '',
  staff_name: '',
  summary: ''
}
const form = reactive({ ...initialForm })

onMounted(async () => {
  await Promise.all([loadAppointments(), loadVisits()])
})

async function loadAppointments() {
  appointments.value = (await appointmentsApi.list()).results
}

async function loadVisits() {
  visits.value = (await visitsApi.list()).results
}

async function saveVisit() {
  await visitsApi.create(form)
  Object.assign(form, initialForm)
  message.value = '探视记录已登记'
  await Promise.all([loadAppointments(), loadVisits()])
}

function formatTime(value) {
  return value ? new Date(value).toLocaleString('zh-CN') : ''
}
</script>
