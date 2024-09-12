from netmiko import ConnectHandler

def exe_command(host, command, commit, enable):
  host = host
  output = {}

  try:
    net_connect = ConnectHandler(**host)
    output.update({"connect": "Host connected"})

    if enable:
      output_enable = net_connect.enable()
      output.update({"enable": output_enable})

    output_command = net_connect.send_config_set(command, exit_config_mode=False)
    output.update({"command": output_command})

    if commit:
      output_commit = net_connect.commit()
      output.update({"commit": output_commit})

  except Exception as err: 
    return err
  
  net_connect.disconnect()

  return(output)