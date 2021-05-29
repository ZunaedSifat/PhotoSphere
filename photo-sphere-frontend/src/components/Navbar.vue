<template>
     <div class="container">
          <div class="logo">
               <img class="icon" src="../../icons/logo-final.svg" alt="" />
          </div>
          <div class="navigation">
               <div class="vertical">
                    <a href="">Exhibition</a>
               </div>
               <div class="vertical">
                    <a href="">MarketPlace</a>
               </div>
               <div class="vertical">
                    <a href="">Profile/Login</a>
               </div>
          </div>
     </div>
</template>

<script>
export default {
     name: 'Navbar',
     props: {
          logged_in: Boolean,
          default: false,
     },
}
</script>

<style scoped>
.container {
     background-color: #6eb4ac80;
     display: flex;
     justify-content: space-between;
     padding: 5px;
}

.icon {
     width: 280px;
}

.navigation {
     display: flex;
     justify-content: space-between;
}

.vertical {
     border-right: 1px solid rgba(0, 0, 0, 0.3);
     height: 12px;
     padding: 20px 15px;
}

a {
     color: rgba(255, 255, 255, 0.95);
     text-decoration: none;
}
</style>
