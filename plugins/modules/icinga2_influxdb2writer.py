#!/usr/bin/python


from ansible.module_utils.basic import AnsibleModule

def main():
	module = AnsibleModule(
		supports_check_mode=True,
		argument_spec = dict(
			state                  = dict(default='present', choices=['present', 'absent']),
			name                   = dict(required=True),
			order                  = dict(default=10, type='int'),
			file                   = dict(default='features-available/influxdb2.conf', type='str'),
			host                   = dict(type='str', required=True),
			port                   = dict(type='int', required=True),
            organization           = dict(type='str', required=True),
            bucket                 = dict(type='str', required=True),
            auth_token             = dict(type='str', required=True),
            ssl_enable             = dict(type='bool'),
            ssl_insecure_noverify  = dict(type='bool'),
            ssl_ca_cert            = dict(type='str'),
            ssl_cert               = dict(type='str'),
            ssl_key                = dict(type='str'),
            host_template          = dict(type='str'),
            service_template       = dict(type='str'),
            enable_send_thresholds = dict(type='bool'),
            enable_send_metadata   = dict(type='bool'),
            flush_interval         = dict(type='str'),
            flush_threshold        = dict(type='int'),
            enable_ha              = dict(type='bool'),
		)
	)

	args = module.params
	name = args.pop('name')
	order = args.pop('order')
	state = args.pop('state')
	file = args.pop('file')

	module.exit_json(changed=False, args=args, name=name, order=str(order), state=state, file=file)

if __name__ == '__main__':
	main()
