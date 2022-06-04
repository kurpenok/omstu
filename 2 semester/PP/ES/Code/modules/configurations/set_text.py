import i18n


def setup(self) -> None:
    self.setWindowTitle(i18n.t("locale.title"))

    self.group_box_registration.setTitle(i18n.t("locale.registration"))
    self.label_surname.setText(i18n.t("locale.surname"))
    self.label_name.setText(i18n.t("locale.name"))
    self.label_patronymic.setText(i18n.t("locale.patronymic"))
    self.label_save_status.setText(i18n.t("locale.none"))
    self.push_button_save_user_info.setText(i18n.t("locale.save_user_info"))

    self.group_box_questions.setTitle(i18n.t("locale.questions"))
    self.push_button_yes.setText(i18n.t("locale.yes"))
    self.push_button_rather_yes.setText(i18n.t("locale.rather_yes"))
    self.push_button_ignorance.setText(i18n.t("locale.ignorance"))
    self.push_button_rather_no.setText(i18n.t("locale.rather_no"))
    self.push_button_no.setText(i18n.t("locale.no"))

