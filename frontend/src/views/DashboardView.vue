<template>
  <section>
    <PageHeader
      eyebrow="工作台"
      title="探视管理概览"
      description="集中查看老人、预约、探视记录和紧急通知的当前状态。"
    />

    <div class="stats-grid">
      <div class="stat-card">
        <span>老人档案</span>
        <strong>{{ residents.length }}</strong>
      </div>
      <div class="stat-card">
        <span>预约总数</span>
        <strong>{{ appointments.length }}</strong>
      </div>
      <div class="stat-card">
        <span>待审核预约</span>
        <strong>{{ pendingCount }}</strong>
      </div>
      <div class="stat-card">
        <span>有效通知</span>
        <strong>{{ activeNotifications }}</strong>
      </div>
    </div>

    <div class="section-grid">
      <article class="panel">
        <h3>近期预约</h3>
        <EmptyState v-if="appointments.length === 0" />
        <ul v-else class="list">
          <li v-for="item in appointments.slice(0, 5)" :key="item.id">
            <div>
              <strong>{{ item.resident.name }}</strong>
              <span>{{ item.family_name }} · {{ item.relationship }}</span>
            </div>
            <em>{{ formatTime(item.visit_time) }}</em>
          </li>
        </ul>
      </article>

      <article class="panel">
        <h3>紧急通知</h3>
        <EmptyState v-if="notifications.length === 0" />
        <ul v-else class="list">
          <li v-for="item in notifications.slice(0, 5)" :key="item.id">
            <div>
              <strong>{{ item.title }}</strong>
              <span>{{ item.content }}</span>
            </div>
            <em :class="['badge', item.level]">{{ levelText[item.level] }}</em>
          </li>
        </ul>
      </article>
    </div>
  </section>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import EmptyState from '../components/EmptyState.vue'
import PageHeader from '../components/PageHeader.vue'
import { appointmentsApi } from '../services/appointments'
import { notificationsApi } from '../services/notifications'
import { residentsApi } from '../services/residents'

const residents = ref([])
const appointments = ref([])
const notifications = ref([])
const levelText = { info: '普通', warning: '重要', critical: '紧急' }

const pendingCount = computed(() => appointments.value.filter((item) => item.status === 'pending').length)
const activeNotifications = computed(() => notifications.value.filter((item) => item.is_active).length)

onMounted(async () => {
  const [residentData, appointmentData, notificationData] = await Promise.all([
    residentsApi.list(),
    appointmentsApi.list(),
    notificationsApi.list()
  ])
  residents.value = residentData.results
  appointments.value = appointmentData.results
  notifications.value = notificationData.results
})

function formatTime(value) {
  return value ? new Date(value).toLocaleString('zh-CN') : ''
}
</script>
