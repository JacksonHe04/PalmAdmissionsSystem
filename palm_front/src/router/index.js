import { createRouter, createWebHashHistory } from "vue-router";
import Login from "@/views/Login/index.vue";
import Layout from "@/views/Layout/index.vue";
import Home from "@/views/Home/index.vue";
import Admin from "@/views/Admin/index.vue";
import Apply from "@/views/Apply/index.vue";
import About from "@/views/About/index.vue";
import Test from "@/views/Test/index.vue";

const hash = createWebHashHistory();
const router = createRouter({
  history: hash,
  routes: [
    {
      path: "/",
      component: Layout,
      children: [
        {
          path: "",
          component: Home,
          meta: { title: "欢迎来到PALM实验室" },
        },
        {
          path: "/apply",
          component: Apply,
          meta: { title: "申请PALM实验室" },
        },
        {
          path: "/login",
          component: Login,
          meta: { title: "登录PALM实验室" },
        },
        {
          path: "/admin",
          component: Admin,
          meta: { title: "PALM实验室后台管理" },
          children: [
            {
              path: "",
              name: "admin-home",
              component: () => import("@/views/Admin/Dashboard/index.vue"),
              meta: { title: "PALM实验室后台管理" },
            },
            {
              path: "dashboard",
              name: "dashboard",
              component: () => import("@/views/Admin/Dashboard/index.vue"),
              meta: { title: "仪表盘" },
            },
            {
              path: "students",
              name: "students",
              component: () => import("@/views/Admin/Students/index.vue"),
              meta: { title: "学生表格" },
            },
            {
              path: "interview",
              name: "interview",
              component: () => import("@/views/Admin/Interview/index.vue"),
              meta: { title: "面试打分" },
            },
            {
              path: "analysis",
              name: "analysis",
              component: () => import("@/views/Admin/Analysis/index.vue"),
              meta: { title: "数据分析" },
            },
            {
              path: "setting",
              name: "setting",
              component: () => import("@/views/Admin/Setting/index.vue"),
              meta: { title: "系统设置" },
            },
            //   profile
            {
              path: "profile",
              name: "profile",
              component: () => import("@/views/Admin/Profile/index.vue"),
              meta: { title: "个人资料" },
            },
          ],
        },
        {
          path: "/about",
          component: About,
          meta: { title: "关于开发者" },
        },
        {
          path: "/test",
          component: Test,
          meta: { title: "开发者测试页面" },
        },
      ],
    },
  ],
  // 路由滚动行为定制
  scrollBehavior() {
    return {
      top: 0,
    };
  },
});

// 假设 isAuthenticated 是一个函数，用于检查用户是否已登录
import { isAuthenticated } from "@/utils/auth"; // 根据实际情况导入

// router.beforeEach((to, from, next) => {
//     document.title = to.meta.title || 'palm';
//
//     // 检查目标路由是否是 /admin
//     if (to.path === '/admin') {
//         // 如果用户未登录，则重定向到 /login
//         if (!isAuthenticated()) {
//             next('/login');
//         } else {
//             // 如果用户已登录，则继续访问 /admin
//             next();
//         }
//     } else {
//         // 对于其他路由，直接放行
//         next();
//     }
// });

export default router;
