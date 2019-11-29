# MIT License
#
# Copyright (c) 2015-2019 Iakiv Kramarenko
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from typing import Union

from selene.new.element import Element
from selene.new.wait import Command


class js:
    @classmethod
    def set_value(cls, value: Union[str, int]) -> Command[Element]:
        def fn(element: Element):
            element.execute_script(
                """return (function(element, text) {
                    var maxlength = element.getAttribute('maxlength') === null
                        ? -1
                        : parseInt(element.getAttribute('maxlength'));
                    element.value = maxlength === -1
                        ? text
                        : text.length <= maxlength
                            ? text
                            : text.substring(0, maxlength);
                    return null;
                })(arguments[0], arguments[1]);""",
                str(value))

        return Command(f'set value by js: {value}', fn)

    @classmethod
    def type(cls, keys: Union[str, int]) -> Command[Element]:
        def fn(element: Element):
            element.execute_script(
                """return (function(element, textToAppend) {
                    var text = element.getAttribute('value') + textToAppend
                    var maxlength = element.getAttribute('maxlength') === null
                        ? -1
                        : parseInt(element.getAttribute('maxlength'));
                    element.value = maxlength === -1
                        ? text
                        : text.length <= maxlength
                            ? text
                            : text.substring(0, maxlength);
                    return null;
                })(arguments[0], arguments[1]);""",
                str(keys))

        return Command(f'set value by js: {keys}', fn)

    scroll_into_view = Command(
        'scroll into view',
        lambda element: element.execute_script(
            """return (function(element) { 
                element.scrollIntoView(true); 
            })(arguments[0]);"""))
