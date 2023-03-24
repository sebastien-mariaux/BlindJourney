import { Application } from "https://unpkg.com/@hotwired/stimulus/dist/stimulus.js"
import messagesController from "./messages_controller.js"
import ajaxSelectController from "./ajax_select_controller.js"
import fileSelectController from "./file_select_controller.js"

window.Stimulus = Application.start()
Stimulus.register("messages", messagesController)
Stimulus.register("ajax-select", ajaxSelectController)
Stimulus.register("file-select", fileSelectController)
