/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/*.{js,jsx}', './src/**/*.{js,jsx}'],
  theme: {
    extend: {},
    fontFamily: {
      'roboto': ['Roboto', 'sans-serif'],
    }
  },
  plugins: [require("daisyui")],
}