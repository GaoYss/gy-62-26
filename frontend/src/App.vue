<template>
  <div class="app-shell">
    <aside class="sidebar">
      <div>
        <p class="eyebrow">Care Visit</p>
        <h1>养老院探视预约系统</h1>
      </div>
      <nav>
        <RouterLink to="/">概览</RouterLink>
        <RouterLink to="/residents">老人信息</RouterLink>
        <RouterLink to="/appointments">家属预约</RouterLink>
        <RouterLink to="/visits">探视记录</RouterLink>
        <RouterLink to="/notifications">紧急通知</RouterLink>
      </nav>
    </aside>
    <main class="content">
      <RouterView />
    </main>
  </div>
</template>
