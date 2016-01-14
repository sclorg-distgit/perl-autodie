%{?scl:%scl_package perl-autodie}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-autodie
Version:        2.22
Release:        3%{?dist}
Summary:        Replace functions with ones that succeed or die
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/autodie/
Source0:        http://www.cpan.org/authors/id/P/PJ/PJF/autodie-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(B)
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(Fcntl)
BuildRequires:  %{?scl_prefix}perl(if)
%if !%{defined perl_bootstrap} && !0%{?scl:1}
BuildRequires:  %{?scl_prefix}perl(IPC::System::Simple) >= 0.12
%endif
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
# Sub::Identify is optional
BuildRequires:  %{?scl_prefix}perl(Tie::RefHash)
# Tests:
BuildRequires:  %{?scl_prefix}perl(FindBin)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
BuildRequires:  %{?scl_prefix}perl(open)
BuildRequires:  %{?scl_prefix}perl(Socket)
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Optional tests:
%if !%{defined perl_bootstrap} && !0%{?scl:1}
BuildRequires:  %{?scl_prefix}perl(BSD::Resource)
%endif
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(B)
Requires:       %{?scl_prefix}perl(Fcntl)
# Keep IPC::System::Simple 0.12 optional
Requires:       %{?scl_prefix}perl(overload)
Requires:       %{?scl_prefix}perl(POSIX)

# Remove falsely detected perl(lib)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(lib\\)$
%if ( 0%{?rhel} && 0%{?rhel} < 7 )
%filter_from_requires /perl(lib)/d
%filter_setup
%endif

%description
The "autodie" and "Fatal" pragma provides a convenient way to replace
functions that normally return false on failure with equivalents that throw an
exception on failure.

However "Fatal" has been obsoleted by the new autodie pragma. Please use
autodie in preference to "Fatal".

%prep
%setup -q -n autodie-%{version}
find -type f -exec chmod -x {} +

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{?scl:"}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc AUTHORS Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Feb 17 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-3
- Updated conditions to work properly for non-RHEL systems
- Resolves: rhbz#1064855

* Thu Dec 12 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-2
- Rebuilt  with newer perl516-build
- Resolves: rhbz#1040838

* Tue Nov 12 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-1
- 2.22 bump

* Wed Apr 03 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.16-1
- SCL package - initial import
