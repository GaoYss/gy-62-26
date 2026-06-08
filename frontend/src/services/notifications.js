import { api } from './api'

export const notificationsApi = {
  list: () => api.get('/notifications/'),
  create: (payload) => api.post('/notifications/', payload),
  update: (id, payload) => api.put(`/notifications/${id}/`, payload),
  remove: (id) => api.delete(`/notifications/${id}/`)
}
