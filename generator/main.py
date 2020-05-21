from templates import generate_template, custom_render_template

if __name__ == '__main__':
    print(custom_render_template(generate_template('test'), a_string='Jjaja', a_number=1))