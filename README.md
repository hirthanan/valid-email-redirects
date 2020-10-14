# Valid Gmail Redirects

Google doesn't treat the . (DOT) character as a character in their email address.  
Use this library to generate all the possible variations of email addresses that can be used  
to redirect to your main email. This tool can be used when registering multiple accounts under  
a single third party service.

## Example

Say my email address is hirth@gmail.com.

This script will generate emails: 
```
['h.irth@gmail.com', 'hi.rth@gmail.com', 'hir.th@gmail.com', 'hirt.h@gmail.com',
 'h.i.rth@gmail.com', 'h.ir.th@gmail.com', 'h.irt.h@gmail.com', 'hi.r.th@gmail.com',
 'hi.rt.h@gmail.com', 'hir.t.h@gmail.com', 'h.i.r.th@gmail.com', 'h.i.rt.h@gmail.com',
 'h.ir.t.h@gmail.com', 'hi.r.t.h@gmail.com', 'h.i.r.t.h@gmail.com']

```

## How do I use it?

Navigate to the directory you want to download the project.  
```
git clone git@github.com:hirthanan/valid-email-redirects.git
cd valid-email-addresses/
python main.py
  >> What email do you want all variations for? hirth@gmail.com
['h.irth@gmail.com',...,]
```

Have fun!
