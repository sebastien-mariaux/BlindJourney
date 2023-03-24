import { Controller } from "https://unpkg.com/@hotwired/stimulus/dist/stimulus.js"


export default class FileSelectController extends Controller {
  static targets = ["display"]

  loadImage(event) {
    this.displayTarget.src = URL.createObjectURL(event.target.files[0])
    this.displayTarget.classList.remove("hidden")
  }

}