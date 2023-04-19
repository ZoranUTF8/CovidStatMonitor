<!-- This code creates a simple contact form with fields for name, email, and message.
The form is submitted to an email address provided in the form action attribute.
The form also includes basic styling using Tailwind CSS classes.
This first-time-use will trigger an email requesting confirmation. -->

<template>
  <div class="flex justify-center items-center h-screen bg-gray-100 p-3">
    <form
      id="contact-form"
      @submit.prevent="sendEmailToApi"
      class="w-full md:w-2/3 lg:w-1/2 bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4"
    >
      <div class="mb-4">
        <label class="block text-gray-700 font-bold mb-2" for="name">
          Name
        </label>
        <input
          required
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="name"
          type="text"
          placeholder="Enter your name"
          v-model="emailData.name"
        />
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 font-bold mb-2" for="email">
          Email
        </label>
        <input
          required
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="email"
          type="email"
          placeholder="Enter your email address"
          v-model="emailData.email"
        />
      </div>
      <div class="mb-6">
        <label class="block text-gray-700 font-bold mb-2" for="message">
          Message
        </label>
        <textarea
          required
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="message"
          rows="6"
          placeholder="Enter your message"
          v-model="emailData.message"
        ></textarea>
      </div>
      <div class="flex items-center justify-center">
        <button
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          type="submit"
          :disabled="loading"
        >
          <template v-if="!loading"> Send Message </template>
          <template v-else> Sending... </template>
        </button>
      </div>
      <div v-if="sent" class="text-green-500 mt-4 text-center">
        {{ sentMessage }}
      </div>
      <div v-if="errorMessage" class="text-red-500 mt-4 text-center">
        {{ errorMessage }}
      </div>
    </form>
  </div>
</template>

<script>
import { CovidApiService } from "@/services/EmailApiService";

export default {
  name: "ContactCorpy",
  data: function () {
    return {
      loading: false,
      errorMessage: null,
      sent: false,
      sentMessage: "",
      emailData: { name: "", email: "", message: "" },
    };
  },

  methods: {
    async sendEmailToApi() {
      try {
        this.loading = true;
        this.sent = false;
        this.errorMessage = null;

        await CovidApiService.sendEmail(this.emailData);

        this.sentMessage = "Email sent successfully!";
        this.sent = true;
        this.emailData = { name: "", email: "", message: "" };

        setTimeout(() => {
          this.sent = false;
        }, 3000);

      } catch (error) {
        this.errorMessage = error;
        setTimeout(() => {
          this.errorMessage = false;
        }, 3000);
        
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>
