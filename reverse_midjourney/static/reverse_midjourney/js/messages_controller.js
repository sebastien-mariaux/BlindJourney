import { Controller } from "https://unpkg.com/@hotwired/stimulus/dist/stimulus.js"


export default class messagesController extends Controller {
  static targets = ["message"]

  connect() {
    setTimeout(() => {
      this.element.style.opacity = '0';
      setTimeout(() => {
        this.element.remove()
      }, 1000)
    }, 5000)
  }
}