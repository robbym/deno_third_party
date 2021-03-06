// Copyright 2018 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "callback.h"

void Foo(base::OnceClosure) {}

void Test() {
  base::OnceClosure cb = base::AdaptCallbackForRepeating(base::BindOnce([] {}));
  Foo(base::AdaptCallbackForRepeating(base::BindOnce([] {})));

  using namespace base;

  OnceClosure cb2 = AdaptCallbackForRepeating(BindOnce([] {}));
  Foo(AdaptCallbackForRepeating(BindOnce([] {})));

  OnceClosure cb3 = base::BindOnce([] {});
}
