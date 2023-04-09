<!-- This code creates a simple contact form with fields for name, email, and message.
The form is submitted to an email address provided in the form action attribute.
The form also includes basic styling using Tailwind CSS classes.-->

<template>
  <div class="flex justify-center items-center h-screen bg-gray-100 p-3">
    <form
      id="contact-form"
      action="https://formsubmit.co/janjiczoran23@gmail.com"
      method="POST"
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
          name="senderName"
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
          name="senderEmail"
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
          name="message"
        ></textarea>
      </div>
      <div class="flex items-center justify-center">
        <button
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          form="contact-form"
          type="submit"
        >
          Send Message
        </button>
      </div>
    </form>
  </div>
</template>

<script></script>
