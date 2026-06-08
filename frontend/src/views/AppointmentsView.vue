<template>
  <section>
    <PageHeader eyebrow="预约" title="家属预约探视" description="家属提交探视申请，工作人员可登记预约状态和备注。" />

    <article class="panel">
      <h3>新建预约</h3>
      <AppointmentForm :model="form" :residents="residents" @submit="saveAppointment" />
      <p v-if="message" class="message">{{ message }}</p>
    </article>

    <article class="panel">
      <h3>预约列表</h3>
      <EmptyState v-if="appointments.length === 0" />
      <div v-else class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>老人</th>
              <th>家属</th>
              <th>探视时间</th>
              <th>人数</th>
              <th>状态</th>
              <th>备注</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in appointments" :key="item.id">
              <td>{{ item.resident.name }} · {{ item.resident.room_number }}</td>
              <td>{{ item.family_name }} · {{ item.family_phone }}</td>
              <td>{{ formatTime(item.visit_time) }}</td>
              <td>{{ item.visitor_count }}</td>
              <td><span :class="['badge', item.status]">{{ statusText[item.status] }}</span></td>
              <td>{{ item.notes || '无' }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </article>
  </section>
</template>

<script setup>
import { onMounted, reactive, ref } from 'vue'
import AppointmentForm from '../components/AppointmentForm.vue'
import EmptyState from '../components/EmptyState.vue'
import PageHeader from '../components/PageHeader.vue'
import { appointmentsApi } from '../services/appointments'
import { residentsApi } from '../services/residents'

const residents = ref([])
const appointments = ref([])
const message = ref('')
const statusText = { pending: '待审核', approved: '已通过', rejected: '已拒绝', completed: '已完成', cancelled: '已取消' }
const initialForm = {
  resident_id: '',
  family_name: '',
  family_phone: '',
  relationship: '',
  visit_time: '',
  visitor_count: 1,
  status: 'pending',
  notes: ''
}
const form = reactive({ ...initialForm })

onMounted(async () => {
  await Promise.all([loadResidents(), loadAppointments()])
})

async function loadResidents() {
  residents.value = (await residentsApi.list()).results
}

async function loadAppointments() {
  appointments.value = (await appointmentsApi.list()).results
}

async function saveAppointment() {
  await appointmentsApi.create(form)
  Object.assign(form, initialForm)
  message.value = '预约已提交'
  await loadAppointments()
}

function formatTime(value) {
  return value ? new Date(value).toLocaleString('zh-CN') : ''
}
</script>
