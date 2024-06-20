from PySide2.QtWidgets import QLineEdit, QPlainTextEdit, QSpinBox, QComboBox, QCheckBox, QLabel, QDoubleSpinBox


def widget_to_setter(widget):
    """
    Get the setter function name of the widget
    :param widget:
    :return:
    """
    if isinstance(widget, QLabel):
        return "setText"
    elif isinstance(widget, QLineEdit):
        return "setText"
    elif isinstance(widget, QPlainTextEdit):
        return "setPlainText"
    elif isinstance(widget, QSpinBox):
        return "setValue"
    elif isinstance(widget, QDoubleSpinBox):
        return "setValue"
    elif isinstance(widget, QComboBox):
        return "setCurrentText"
    elif isinstance(widget, QCheckBox):
        return "setChecked"


def widget_to_signal(widget):
    """
    Get the signal name of the widget what is emitted when the content is changed.
    :param widget:
    :return:
    """
    if isinstance(widget, QLineEdit):
        return "textChanged"
    elif isinstance(widget, QPlainTextEdit):
        return "textChanged"
    elif isinstance(widget, QSpinBox):
        return "valueChanged"
    elif isinstance(widget, QDoubleSpinBox):
        return "valueChanged"
    elif isinstance(widget, QComboBox):
        return "currentTextChanged"
    elif isinstance(widget, QCheckBox):
        return "stateChanged"


def widget_to_getter(widget):
    """
    Get the getter function name of the widget
    :param widget:
    :return:
    """
    if isinstance(widget, QLineEdit):
        return "text"
    elif isinstance(widget, QPlainTextEdit):
        return "toPlainText"
    elif isinstance(widget, QSpinBox):
        return "value"
    elif isinstance(widget, QDoubleSpinBox):
        return "value"
    elif isinstance(widget, QComboBox):
        return "currentText"
    elif isinstance(widget, QCheckBox):
        return "isChecked"
