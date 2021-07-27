<template>
    <el-dialog
        v-model="dialog"
        title="Create New Exhibition"
        width="40%"
        show-close
        :before-close="onClose"
    >
        <el-form ref="form" :model="form" size="small" status-icon>
            <el-form-item label="Phone" prop="phone">
                <el-input v-model="form.phone"></el-input>
            </el-form-item>
            <el-form-item label="Address" prop="address">
                <el-input v-model="form.address"></el-input>
            </el-form-item>
            <el-form-item label="City" prop="city">
                <el-input v-model="form.city"></el-input>
            </el-form-item>
            <el-form-item style="text-align: center">
                <el-button
                    type="primary"
                    style="padding: 8px 80px; margin: 16px"
                    :loading="loading"
                    @click="onSubmit"
                    >PROCEED TO PAYMENT
                </el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>
import { placeOrder } from "@/api/order.api";

export default {
    name: "Photo Purchase",
    props: {
        dialog: {
            type: Boolean,
            default: false,
        },
        photo: {
            type: Number,
            required: true,
        },
    },
    data() {
        return {
            loading: false,
            form: {
                phone: "",
                address: "",
                city: "",
            },
        };
    },
    methods: {
        onClose(done) {
            this.$emit("close");
            done();
        },
        async onSubmit() {
            this.loading = true;
            try {
                const data = {
                    photo: this.photo,
                    phone: this.form.phone,
                    address: this.form.address,
                    city: this.form.city,
                };

                const response = await placeOrder(data);
                console.log(response);
                window.open(response.data.redirection_url);
            } catch (error) {
                console.log(error.response);
            } finally {
                this.loading = false;
                this.$emit("close");
            }
        },
    },
};
</script>

<style>
</style>