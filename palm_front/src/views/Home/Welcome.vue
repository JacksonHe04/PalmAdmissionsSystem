<template>
  <div class="welcome-section">
    <h1>欢迎来到 PALM 实验室</h1>
    <router-link to="/apply">
      <button class="apply-button">立即申请</button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'Welcome',
};
</script>

<style scoped>
.welcome-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 2rem;
  background-color: rgba(245, 246, 250, 0.5);
  border-radius: 50px;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
  width: 60%;
  height: 400px;
}

.apply-button {
  margin-top: 30px;
  padding: 1rem 2rem;
  font-size: 2rem;
  color: #fff;
  background-color: #5d7faa;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.apply-button:hover {
  background-color: #5d7faa;
  opacity: 70%;
}
</style>
