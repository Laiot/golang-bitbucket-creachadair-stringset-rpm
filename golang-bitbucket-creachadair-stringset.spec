# Generated by go2rpm 1.6.0
%bcond_without check

# https://bitbucket.org/creachadair/stringset
%global goipath         bitbucket.org/creachadair/stringset
%global forgeurl        https://bitbucket.org/creachadair/stringset
%global commit          1f9a78a15a647874b03da57f7588805b47b198cf
Version:                0.0.10

%gometa

%global common_description %{expand:
A lightweight set-of-strings implementation based on the Go built-in map type.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        A lightweight set-of-strings implementation based on the Go built-in map type, providing some common set-like operations

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
BuildArch: noarch
%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
