import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('101.132.183.16', port=22, username='root', password='Zhangjiang2025@@@', timeout=10)

sftp = ssh.open_sftp()
with sftp.file('/etc/nginx/sites-available/default.bak_astro', 'r') as f:
    orig = f.read().decode('utf-8')

astro_block = """
    # ---- 4. 人类图高精排盘与商业解读系统 (astro) ----
    location = /astro {
        return 301 /astro/;
    }

    location /astro/ {
        proxy_pass http://127.0.0.1:8008/;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_read_timeout 120s;
        proxy_connect_timeout 10s;
        proxy_send_timeout 120s;
    }
"""

last_brace_idx = orig.rfind('}')
new_conf = orig[:last_brace_idx] + astro_block + orig[last_brace_idx:]

with sftp.file('/etc/nginx/sites-available/default', 'w') as f:
    f.write(new_conf)
sftp.close()

stdin, stdout, stderr = ssh.exec_command('nginx -t && systemctl reload nginx')
out = stdout.read().decode('utf-8')
err = stderr.read().decode('utf-8')
print('STDOUT:\n', out)
print('STDERR:\n', err)
ssh.close()
