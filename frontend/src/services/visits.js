import { api } from './api'

export const visitsApi = {
  list: () => api.get('/visits/'),
  create: (payload) => api.post('/visits/', payload),
  update: (id, payload) => api.put(`/visits/${id}/`, payload),
  remove: (id) => api.delete(`/visits/${id}/`)
}
