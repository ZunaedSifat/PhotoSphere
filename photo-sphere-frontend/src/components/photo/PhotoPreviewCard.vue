
<template>
    <el-card
        :body-style="{ padding: '0px', width: '200px' }"
        @click="viewDetails"
    >
        <img :src="photo.image" class="image" />
        <div style="padding: 14px">
            <span>{{ photo.title }}</span>
            <!-- <div class="bottom">
                <time class="time">{{ currentDate }}</time>
                <el-button type="text" class="button">Operating</el-button>
            </div> -->
        </div>
    </el-card>
</template>

<script>
export default {
    props: {
        photo: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            currentDate: new Date(),
        };
    },
    methods: {
        viewDetails() {
            this.$router.push({
                name: "Photo-Details",
                params: { id: this.photo.id },
            });
        },
    },
};
</script>

<style>
.time {
    font-size: 13px;
    color: #999;
}

.bottom {
    margin-top: 13px;
    line-height: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.button {
    padding: 0;
    min-height: auto;
}

.image {
    width: 100%;
    display: block;
}
</style>
